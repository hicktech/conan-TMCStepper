#!/usr/bin/env bash

readonly sourcedir="${SOURCE_DIR:-${PWD}}"
readonly builddir="${BUILD_DIR:-${sourcedir}/build}"

readonly conanpath="${CONAN_PATH:-${sourcedir}}"
readonly conanuser="${CONAN_USER:-hicktech}"
readonly conanchannel="${CONAN_CHANNEL:-stable}"

remote="${CONAN_REMOTE:-particle-bintray}"

if [[ "$1" != "quick" ]]; then
  rm -rf "$builddir"
fi

if [ ! -d ${builddir} ]; then mkdir -p "$builddir"; fi

conan source . -sf ${builddir}
conan export-pkg . "$conanuser/$conanchannel" -sf ${builddir} -f

#conan upload "$pkg/$version@$conanuser/$conanchannel" -c -r "$remote" --all
