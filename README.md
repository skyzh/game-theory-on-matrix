# A Game

```bash
echo "5 1.02" | make run > visualization/result.js
```

Then open visualization/index.html, save result.svg

```bash
pip3 install cairosvg
cairosvg result.svg -o result_5_1.02.png
```