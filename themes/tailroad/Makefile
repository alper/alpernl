# https://github.com/kaushikgopal/henry-hugo/blob/master/Makefile
default: run

# Set default warning mode if not specified
# permitted values debug|info|warn|error
# e.g. usage from make cli:
#  		make build log=debug
#  		make build-site log=debug
log ?= warn

help:		## list out commands with descriptions
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

build:		## hugo build & compile css (one-time)
	@make site css

run: ##            run Hugo server & watch Tailwind CSS compiler
	@make -j2 run-site run-css
	# --jobs=2 parallelizes the commands

site:		## hugo compile build
	@hugo \
		build \
		--cleanDestinationDir --gc --minify --printI18nWarnings --buildDrafts \
		--logLevel $(log)

css:		## compile Tailwind CSS
	@npx @tailwindcss/cli \
		-i ./assets/css/main.css  \
		-o ./assets/css/styles.css

run-css:	## run & watch Tailwind CSS compiler
	@npx @tailwindcss/cli \
		-i ./assets/css/main.css  \
		-o ./assets/css/styles.css --watch

run-site:	## run Hugo server
	@hugo \
		server \
		--source exampleSite \
		--themesDir ../.. \
	    --disableFastRender \
		--cleanDestinationDir --gc --minify --printI18nWarnings --buildDrafts \
		--logLevel $(log)

clean:  ## cleans public folder
	rm -rf public
	rm  -f assets/css/styles.css