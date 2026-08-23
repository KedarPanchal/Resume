from types import SimpleNamespace
import yaml


class YamlParser:
    def __init__(self, path: str):
        self._data = self._load_dict(path)

    def _load_dict(self, path: str) -> dict:
        with open(path, 'r') as yaml_file:
            return yaml.safe_load(yaml_file)
    
    def _load_helper(self, source: dict, key: str, value: dict | None) -> dict | list | str | None:
        # If empty dict is passed, assume everything should be returned
        if value is None:
            return source[key] if key in source else None
        
        # Assume result is a dictionary unless specified otherwise
        result = {}
        # If "include" is not specified or is set to "all", return the entire source for that key
        if "include" not in value or value["include"] == "all":
                result = source[key] if key in source else None
        elif isinstance(value["include"], list):
            for item in value["include"]:
                # Add item raw to result if it's a string
                if isinstance(item, str):
                    if item not in source[key]:
                        raise ValueError(f"Item '{item}' not found in source for key '{key}'.")
                    result[item] = source[key][item]
                # Index into the source dictionary if item is an integer
                elif isinstance(item, int):
                    target_key = list(source[key].keys())[item]
                    result[target_key] = source[key][target_key]
                # Handle nested dictionaries
                elif isinstance(item, dict):
                    inner_key = next(iter(item))
                    result[inner_key] = self._load_helper(source[key], inner_key, item[inner_key])
                else:
                    raise ValueError(f"Expected a str, int, or dict in 'include' for key '{key}', but got {type(item)}.")
        else:
            raise ValueError(f"Expected a list or 'all' for 'include' in key '{key}', but got {type(value['include'])}.")
        
        # Remove excluded items from the result if "exclude" is specified
        if "exclude" in value:
            if not isinstance(value["exclude"], list) and value["exclude"] != "all":
                raise ValueError(f"Expected a list for 'exclude' in key '{key}', but got {type(value['exclude'])}.")
            if value["exclude"] == "all":
                return None
            exclude_set = set(value["exclude"])
            # Handle based on whether a list or dictionary was included
            if isinstance(result, dict):
                result = {k: v for k, v in result.items() if k not in exclude_set}
            elif isinstance(result, list):
                result = [item for item in result if item not in exclude_set]
        return result if result else None
    
    def _to_object(self, data: dict) -> SimpleNamespace:
        objectified = SimpleNamespace(**data)
        for key, value in data.items():
            if isinstance(value, dict):
                setattr(objectified, key, self._to_object(value))
            elif isinstance(value, list):
                setattr(objectified, key, [self._to_object(item) if isinstance(item, dict) else item for item in value])
        return objectified

    def load(self, view_path: str) -> SimpleNamespace:
        view = self._load_dict(view_path)
        
        result_dict = {}
        for key, value in view.items():
            if not isinstance(value, dict) and value is not None:
                raise ValueError("Top-level values in the view file must be fields.")
            result = self._load_helper(self._data, key, value)
            if result is not None:
                result_dict[key] = result
        return self._to_object(result_dict)
