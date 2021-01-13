
var w = 600;
var h = 400;
var n;

function setup(){
  // ...
  createCanvas(w, h).parent('canvasHolder');
  // ...
  n = createSlider(1, 1000, 500, 1).parent('nParticles');
  // ...
}
