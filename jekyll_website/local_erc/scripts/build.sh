#! /bin/bash

DEPLOY_REPO="https://${GITHUB_TOKEN}@github.com/${GITHUB_REPO}.git"

set -e

function main {
	cleansite
	get_current_site
	build_site
	echo "Build succesful"
	deploy
}

function cleansite { 
echo "cleaning _site folder"
if [ -d "_site" ]; then rm -Rf _site; fi 
}

function get_current_site { 
echo "getting latest site"
git clone --depth 1 $DEPLOY_REPO _site 
}

function build_site { 
echo "building site"
bundle exec jekyll build
}

function deploy {
	echo "deploying changes"
	#commented out because I want to publish pull requests
	if false
		then
		if [ -z "$TRAVIS_PULL_REQUEST" ]; then
			echo "except don't publish site for pull requests"
			exit 0
		fi  
	fi
	#commented out^

	if [ "$TRAVIS_BRANCH" != "master" ]; then
		echo "except we should only publish the master branch. stopping here"
		exit 0
	fi

	echo "configuring username/email"
	git config --global user.name "Travis CI"
	git config --global user.email "aryanagal98@gmail.com"
	
	echo "applying ghpages.patch"
	git apply ghpages.patch
	
	echo "jekyll building"
	bundle exec jekyll build

	echo "committing changes"
	cd _site
	git init
	git add -A
	git commit -m "Lastest site built on successful travis build $TRAVIS_BUILD_NUMBER auto-pushed to github"
	
	echo "Pushing changes"
	git push --quiet -f "https://${GITHUB_TOKEN}@github.com/${GITHUB_REPO}" master:master > /dev/null 2>&1

	echo "Push successful"
}


main