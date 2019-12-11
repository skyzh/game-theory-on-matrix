const BLOCK_SIZE = 7
const N = 50
const WIDTH = BLOCK_SIZE * N
const HEIGHT = BLOCK_SIZE * N
const TEXT_HEIGHT = 30

let set_m = () => {}

$(document).ready(() => {
    let epoch = 0
    let updates = []
    const MM = [5, 10, 20, 50, 100, 200]
    MM.forEach(M => {
        const $graph = d3.select('#graph')
            .append('svg')
            .attr('class', 'simulation')
            .attr('width', WIDTH)
            .attr('height', HEIGHT + TEXT_HEIGHT)
        let coop = window[`data_${M}`]
        let matrix = []
        for (let i = 0; i < N * N; i++) matrix.push(0)
        const next_epoch = () => {
            key = `epoch${epoch}`
            if (key in coop) {
                coop[key].forEach(i => {
                    matrix[i] = 1 - matrix[i]
                })
                return true
            } else {
                return false
            }
        }
        const update = () => {
            if(next_epoch()) {
                $graph.selectAll('.prison')
                    .data(matrix)
                    .enter()
                        .append('rect')
                        .attr('class', 'prison')
                $graph.selectAll('.prison')
                    .attr('x', (d, idx) => (idx % N) * BLOCK_SIZE)
                    .attr('y', (d, idx) => Math.floor(idx / N) * BLOCK_SIZE + TEXT_HEIGHT)
                    .attr('width', BLOCK_SIZE)
                    .attr('height', BLOCK_SIZE)
                    .attr('style', d => (d == 0 ? "fill:#EF8A62" : "fill:white"))
            }
        }
        updates.push(update)
        $graph.append("text").attr("x", 0).attr("y", 20).text(`M = ${M}`)
    })
    const update = () => {
        updates.forEach(u => u())
        epoch += 10
        setTimeout(() => update(), 1)
        $("#epoch").text(`Epoch ${epoch}`)
    }
    update()

})
