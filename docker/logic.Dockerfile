FROM python:3

RUN mkdir docker_root
RUN cd docker_root
WORKDIR /docker_root
RUN mkdir logic

ADD /logic /docker_root/logic
ADD requirements.txt /docker_root
ADD /fonts/calibri.ttf /usr/share/fonts/truetype/calibri/calibri.ttf
ADD /fonts/comic_sans.ttf /usr/share/fonts/truetype/comic_sans/comic_sans.ttf
ADD /fonts/futura.ttf /usr/share/fonts/truetype/futura/futura.ttf
ADD /fonts/inconsolata.ttf /usr/share/fonts/truetype/inconsolata/inconsolata.ttf
ADD /fonts/open_sans.ttf /usr/share/fonts/truetype/open_sans/open_sans.ttf
ADD /fonts/papyrus.ttf /usr/share/fonts/truetype/papyrus/papyrus.ttf
ADD /fonts/roboto.ttf /usr/share/fonts/truetype/roboto/roboto.ttf
ADD /fonts/times_newer_roman.ttf /usr/share/fonts/truetype/times_newer_roman/times_newer_roman.ttf
ADD /fonts/wingdings.ttf /usr/share/fonts/truetype/wingdings/wingdings.ttf

RUN pip install -r requirements.txt

EXPOSE 5000


CMD ["python", "-m", "logic.flask_create"]