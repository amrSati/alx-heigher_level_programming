#!/usr/bin/node

const arg = process.argv.slice(2)[0];

if (isNaN(arg)) console.log('Not a number');
else {
  const num = parseInt(arg);
  console.log(`My number: ${num}`);
}
