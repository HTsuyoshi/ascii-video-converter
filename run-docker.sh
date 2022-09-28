#!/bin/bash

function usage() {
	echo 'usage:'
	echo '    ./run-docker video [ascii-video parameters]'
	echo ''
	echo 'Program help:'
	echo ''
	docker run --rm ascii-video:1.0 --help
	exit 1
}

[[ -z "$1" ]] && usage # If has a video
[[ $(ls $1) ]] || usage # If the video exists

VIDEO_NAME="$(echo $1 | awk -F '/' '{print $(NF)}')" # Get video name
ARGUMENTS="${@:2}" # Program arguments

docker run --rm -it -v "$(ls $1)":/create-video/$VIDEO_NAME -v /tmp:/tmp ascii-create-video:1.0 $VIDEO_NAME $ARGUMENTS || exit 1 && \
	ARGUMENTS="-r=n -v=1" && \ # Program arguments
	docker run --rm -it -v /tmp:/tmp ascii-run-video:1.0 $ARGUMENTS && exit 0

