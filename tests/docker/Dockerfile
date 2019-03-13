FROM openjdk:8-jre-stretch

# Install sudo
RUN apt-get -y update && apt-get -y install sudo build-essential

# Get Mooshak installer
RUN wget http://mooshak2.dcc.fc.up.pt/install/MooshakInstaller.jar

# Install Mooshak with configs in install.config
ADD install.conf /
RUN grep "^[^#]" install.conf | java -jar MooshakInstaller.jar -cui

# Fix permissions
RUN chmod +x /home/mooshak/tomcat8/bin/*.sh

# Expose port 8080
EXPOSE 8080

# Data volume
VOLUME /home/mooshak/data

# Run Mooshak server
ENTRYPOINT ["/home/mooshak/tomcat8/bin/catalina.sh", "run"]