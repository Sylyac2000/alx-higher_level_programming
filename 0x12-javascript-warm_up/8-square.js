#!/usr/bin/node

const taille = parseInt(process.argv[2]);

if (isNaN(taille)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < taille; i += 1) {
    console.log('X'.repeat(taille));
  }
}
