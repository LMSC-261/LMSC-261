let music;

function preload() {
  soundFormats('mp3', 'ogg');
  music = loadSound('static/snds/CHIC - Le Freak');
}

function setup() {
  let canvas = createCanvas(windowWidth, 300);
  canvas.parent('heading');
  
  // Resize the canvas after it is attached
  let card = document.querySelector('#heading');
  resizeCanvas(card.offsetWidth, 300);

  // Set the canvas property
  background(0);
  noStroke();
}

function draw() {
  // Compute the width and height for each rectangle using the canvas size
  let spacing = 20; // Used to space each rectangle
  let boxHeight = ((height - spacing) / 4) - spacing;
  let numRows = Math.floor(width / (boxHeight + spacing));
  let boxWidth = ((width - spacing) / numRows) - spacing;

  for(let y = 0; y < 4; y++){ // Limit to four rectangles vertically
    for(let x = 0; x < numRows; x++){
      fill(color(random(0,255),random(0,255),random(0,255)));
      rect(spacing + x * (spacing + boxWidth), spacing + y * (spacing + boxHeight), boxWidth, boxHeight); 
    }
  }

  noLoop();
}

function windowResized() {
  let card = document.querySelector('#heading');
  resizeCanvas(card.offsetWidth, 300);
  loop();
}

document.addEventListener("DOMContentLoaded", function(event) { 
  let overlay = document.querySelector('#heading-overlay');
  overlay.addEventListener('click', function(){
    if(!music.isPlaying()){
      music.play();
    }
    else {
      music.stop();
    }
  });
});