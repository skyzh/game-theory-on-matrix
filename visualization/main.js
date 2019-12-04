const BLOCK_SIZE = 10
const N = 50
const WIDTH = BLOCK_SIZE * N
const HEIGHT = BLOCK_SIZE * N
$(document).ready(() => {
    const $graph = d3.select('#graph')
        .append('svg')
        .attr('width', WIDTH)
        .attr('height', HEIGHT)
    const coop = data.data
    $graph.selectAll('.prison')
        .data(coop)
        .enter()
            .append('rect')
            .attr('class', 'prison')
            .attr('x', (d, idx) => (idx % N) * BLOCK_SIZE)
            .attr('y', (d, idx) => Math.floor(idx / N) * BLOCK_SIZE)
            .attr('width', BLOCK_SIZE)
            .attr('height', BLOCK_SIZE)
            .attr('style', d => (d == 0 ? "fill:blue" : "fill:pink"))
    saveSvg($('svg')[0], "result.svg")
})

function saveSvg(svgEl, name) {
    svgEl.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    var svgData = svgEl.outerHTML;
    var preface = '<?xml version="1.0" standalone="no"?>\r\n';
    var svgBlob = new Blob([preface, svgData], {type:"image/svg+xml;charset=utf-8"});
    var svgUrl = URL.createObjectURL(svgBlob);
    var downloadLink = document.createElement("a");
    downloadLink.href = svgUrl;
    downloadLink.download = name;
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
}
