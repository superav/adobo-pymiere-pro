FROM python:3.8

# WORKDIR /opt/build

# ENV OPENCV_VERSION="4.5.1"

# RUN apt-get -qq update \
#     && apt-get -qq install -y --no-install-recommends \
#     build-essential \
#     cmake \
#     git \
#     wget \
#     unzip \
#     yasm \
#     pkg-config \
#     libswscale-dev \
#     libtbb2 \
#     libtbb-dev \
#     libjpeg-dev \
#     libpng-dev \
#     libtiff-dev \
#     libopenjp2-7-dev \
#     libavformat-dev \
#     libpq-dev \
#     && pip install numpy \
#     && wget -q https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip -O opencv.zip \
#     && unzip -qq opencv.zip -d /opt \
#     && rm -rf opencv.zip \
#     && cmake \
#     -D BUILD_TIFF=ON \
#     -D BUILD_opencv_java=OFF \
#     -D WITH_CUDA=OFF \
#     -D WITH_OPENGL=ON \
#     -D WITH_OPENCL=ON \
#     -D WITH_IPP=ON \
#     -D WITH_TBB=ON \
#     -D WITH_EIGEN=ON \
#     -D WITH_V4L=ON \
#     -D BUILD_TESTS=OFF \
#     -D BUILD_PERF_TESTS=OFF \
#     -D CMAKE_BUILD_TYPE=RELEASE \
#     -D CMAKE_INSTALL_PREFIX=$(python3.8 -c "import sys; print(sys.prefix)") \
#     -D PYTHON_EXECUTABLE=$(which python3.8) \
#     -D PYTHON_INCLUDE_DIR=$(python3.8 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
#     -D PYTHON_PACKAGES_PATH=$(python3.8 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") \
#     /opt/opencv-${OPENCV_VERSION} \
#     && make -j$(nproc) \
#     && make install \
#     && rm -rf /opt/build/* \
#     && rm -rf /opt/opencv-${OPENCV_VERSION} \
#     && rm -rf /var/lib/apt/lists/* \
#     && apt-get -qq autoremove \
#     && apt-get -qq clean

RUN mkdir docker_root
RUN cd docker_root
WORKDIR /docker_root
RUN mkdir logic

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

# RUN apt-get update ##[edited]
# RUN apt-get install ffmpeg libsm6 libxext6  -y
# RUN apt-get install -y libgl1-mesa-dev
# RUN apt-get install libsm6 libxrender1 libfontconfig1
# RUN python3 -m pip install opencv-contrib-python
# RUN apt install libgl1-mesa-glx
# RUN apt-get install -y python3-opencv

# RUN apt-get install software-properties-common
# RUN add-apt-repository ppa:deadsnakes/ppa
# RUN apt-get update
# RUN apt-get install python3.8
RUN pip3 install -r requirements.txt


EXPOSE 5000


CMD ["python3", "-m", "logic.flask_create"]