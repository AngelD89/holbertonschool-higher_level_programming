#!/usr/bin/node
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const a = process.argv[2];
const b = process.argv[3];
console.log(add(a, b));
