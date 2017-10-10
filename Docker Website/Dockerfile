FROM ubuntu:16.04

RUN mkdir /website
#Gemfile is required so make sure you have your Gemfile in your folder
ADD Gemfile /website

RUN apt-get -y update && apt-get install -y \
	ruby \
	gem \
	git \
	bundler \
	jekyll 	
 
RUN apt-get -y install build-essential patch ruby-dev zlib1g-dev liblzma-dev
RUN gem install ffi -v '1.9.18'
RUN gem install nokogiri

VOLUME /website
WORKDIR /website

RUN bundle install

EXPOSE 4000

CMD ["bundle", "exec", "jekyll", "serve", "--host=0.0.0.0"]
