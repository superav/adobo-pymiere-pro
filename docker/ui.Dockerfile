FROM node

RUN mkdir docker_root
RUN cd docker_root
RUN mkdir ui

WORKDIR /docker_root/ui

RUN npm install

EXPOSE 3000


CMD ["npm", "start"]