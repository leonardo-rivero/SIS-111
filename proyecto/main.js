// Constante con el mapa fijo (25x25)


// 0 = vacío
// 1 = muro sólido
// 2 = camino
// 3 = ladrillo destructible
// 4 = agua
// 5 = base/objetivo

const LEVELS = {
  1: [
  [1,1,1,1,1,1,1,1,1,1], // fila superior: muro
  [1,2,2,2,2,2,2,2,2,1], // camino abierto
  [1,2,3,3,0,0,3,3,2,1], // ladrillos y huecos
  [1,2,0,4,4,4,4,0,2,1], // agua en el centro
  [1,2,3,0,5,5,0,3,2,1], // base protegida
  [1,2,0,4,4,4,4,0,2,1], // simétrico al de arriba
  [1,2,3,3,0,0,3,3,2,1], // ladrillos otra vez
  [1,2,2,2,2,2,2,2,2,1], // camino abierto
  [1,2,2,2,2,2,2,2,2,1], // camino abierto
  [1,1,1,1,9,1,1,1,1,1], // fila inferior: muro
],
2: [
  [1,1,1,1,1,1,1,1,1,1], // fila superior: muro
  [1,2,2,2,2,2,2,2,2,1], // camino abierto
  [1,2,3,3,0,0,3,3,2,1], // ladrillos y huecos
  [1,2,0,4,4,4,4,0,2,1], // agua en el centro
  [1,2,3,0,5,5,0,3,2,1], // base protegida
  [1,2,0,4,4,4,4,0,2,1], // simétrico al de arriba
  [1,2,3,3,0,0,3,3,2,1], // ladrillos otra vez
  [1,2,2,2,2,2,2,2,2,1], // camino abierto
  [1,2,2,2,2,2,2,2,2,1], // camino abierto
  [1,1,1,1,9,1,1,1,1,1], // fila inferior: muro
],
3: [
  [1,1,1,1,1,1,1,1,1,1], // fila superior: muro
  [1,2,2,2,2,2,2,2,2,1], // camino abierto
  [1,2,3,3,0,0,3,3,2,1], // ladrillos y huecos
  [1,2,0,4,4,4,4,0,2,1], // agua en el centro
  [1,2,3,0,5,5,0,3,2,1], // base protegida
  [1,2,0,4,4,4,4,0,2,1], // simétrico al de arriba
  [1,2,3,3,0,0,3,3,2,1], // ladrillos otra vez
  [1,2,2,2,2,2,2,2,2,1], // camino abierto
  [1,2,2,2,2,2,2,2,2,1], // camino abierto
  [1,1,1,1,9,1,1,1,1,1], // fila inferior: muro
]

};


