#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const args = process.argv;

const url = args[2];
const filename = args[3];
request(url).pipe(fs.createWriteStream(filename));
