function init() {

  const canvas = document.querySelector('#page_canvas')
  canvas.height = window.innerHeight
  canvas.width = window.innerWidth
  const ctx = canvas.getContext('2d')


  const shape = {
    coords: [],
    complete: false
  }

  function getMouseCoords(event) {
    return {
      x: event.clientX,
      y: event.clientY
    }
  }

  function drawShape() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    ctx.beginPath()
    ctx.fillStyle = 'black'
    for (let i = 0; i < shape.coords.length; i++) {
      const v = shape.coords[i]
      if (i === 0) {
        ctx.moveTo(v.x, v.y)
      } else {
        ctx.lineTo(v.x, v.y)
      }
      // ctx.beginPath()
      ctx.arc(v.x, v.y, 5, 0, 2 * Math.PI,)
      ctx.stroke()
      // shape.coords[i]
    }
    ctx.closePath()
  }

  function finalSegment(coords) {
    const shapeFinalV = shape.coords[shape.coords.length - 1]
    ctx.beginPath()
    ctx.moveTo(shapeFinalV.x, shapeFinalV.y)
    ctx.lineTo(coords.x, coords.y)
    ctx.stroke()
    ctx.closePath()
  }

  function shapeEdgeDraw(coords) {

    drawShape()
    finalSegment(coords)

  }

  function checkIfInCircle(coords) {
    const vector = {
      x: coords.x - shape.coords[0].x,
      y: coords.y - shape.coords[0].y
    }

    const length = ((vector.x ** vector.x) + (vector.y ** vector.y)) ** 0.5

    return length < 5
  }


  function mousemove(event) {
    if (shape.coords.length < 1 || shape.complete === true) return
    const coords = getMouseCoords(event)

    shapeEdgeDraw(coords)
  }

  function clickEvent(event) {
    if (shape.complete) return
    const coords = getMouseCoords(event)

    if (shape.coords.length >= 2) {
      if (checkIfInCircle(coords)) {
        shape.complete = true
        drawShape()
        return
      }
    }
    shape.coords.push(coords)

    drawShape()

  }
  canvas.addEventListener('mousemove', mousemove)
  canvas.addEventListener('click', clickEvent)

}

window.addEventListener('DOMContentLoaded', init)