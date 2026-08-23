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

        result = {}
        if "include" not in value or value["include"] == "all":
                result = source[key] if key in source else None
        elif isinstance(value["include"], list):
            for item in value["include"]:
                if isinstance(item, str):
                    if item not in source[key]:
                        raise ValueError(f"Item '{item}' not found in source for key '{key}'.")
                    result[item] = source[key][item]
                elif isinstance(item, int):
                    target_key = list(source[key].keys())[item]
                    result[target_key] = source[key][target_key]
                elif isinstance(item, dict):
                    inner_key = next(iter(item))
                    result[inner_key] = self._load_helper(source[key], inner_key, item[inner_key])
                else:
                    raise ValueError(f"Expected a str, int, or dict in 'include' for key '{key}', but got {type(item)}.")
        else:
            raise ValueError(f"Expected a list or 'all' for 'include' in key '{key}', but got {type(value['include'])}.")

        if "exclude" in value:
            if not isinstance(value["exclude"], list) or value["exclude"] == "all":
                raise ValueError(f"Expected a list for 'exclude' in key '{key}', but got {type(value['exclude'])}.")
            if value["exclude"] == "all":
                return {}
            exclude_set = set(value["exclude"])
            if isinstance(result, dict):
                result = {k: v for k, v in result.items() if k not in exclude_set}
            elif isinstance(result, list):
                result = [item for item in result if item not in exclude_set]
        return result if result else None


    def load(self, view_path: str):
        view = self._load_dict(view_path)
        
        result_dict = {}
        for key, value in view.items():
            if not isinstance(value, dict) and value is not None:
                raise ValueError("Top-level values in the view file must be fields.")
            result = self._load_helper(self._data, key, value)
            if result is not None:
                result_dict[key] = result
        return result_dict
