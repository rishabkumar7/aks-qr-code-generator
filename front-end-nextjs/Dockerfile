FROM node:18

# Set the working directory
WORKDIR /usr/src/app

# Install dependencies
COPY package.json ./
RUN npm install

# Bundle app source
COPY . .

# Build the app
RUN npm run build

# Start the app
CMD [ "npm", "start" ]