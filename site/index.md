---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
title: Kedar Panchal
---

{% capture left_column %}
Howdy!

I'm a **computer science** and **cybersecurity honors** student at **Texas A&M 
University** with a passion for robotics, software engineering, and artificial 
intelligence. I enjoy exploring creative (and sometimes unorthodox) solutions 
and tools to  solve problems, and I love learning about the field of computer 
science as a whole.

My work experience spans a **variety of fields**, including software 
engineering, AI agent development, and automation in a **range of industries** 
such as defense, web development, and real estate.

I'm currently conducting research at the **Distributed AI and Robotics Lab 
(DAIR)** at Texas A&M under the guidance of Dr. Dylan Shell, where I am 
developing  coverage algorithms for coordinating multiple, blind robots with 
limited rotational precision.
{% endcapture %}

{% capture right_column %}
![Kedar Panchal]({{ site.baseurl }}/assets/images/me.png){: style="width: 75%; max-width: 300px; height: auto; margin-top: 45px;"}
{% endcapture %}

{% include two-column.html col1=left_column col2=right_column %}
