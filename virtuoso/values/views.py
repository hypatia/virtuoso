from django.shortcuts import render, get_object_or_404
import json
from values.models import Value

def index(request):
    values_list = Value.objects.all().order_by('-frequency')
    values = []
    total_count = 0
    for v in values_list:
    	total_count = total_count + int(v.frequency)
    size_ratio = len(values_list) / total_count * 4
    for value in values_list:
    	values.append({
    			"text": value.value,
    			"size": int(value.frequency * size_ratio)
    		})
    script = """<script type="text/javascript" charset="utf-8">
  var fill = d3.scale.category20();
  var words = %s

  d3.layout.cloud().size([600, 600])
      .words(words)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function(d) { return d.size; })
      .on("end", draw)
      .start();

  function draw(words) {
    d3.select("body").append("svg")
        .attr("width", 800)
        .attr("height", 800)
      .append("g")
        .attr("transform", "translate(400,400)")
      .selectAll("text")
        .data(words)
      .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", "Impact")
        .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
          return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; });
  }
</script>""" % json.dumps(values)
    context = {'values_list': values_list, 'script': script}
    return render(request, 'values/index.html', context)

def detail(request, value_id):
    value = get_object_or_404(Value, pk=value_id)
    return render(request, 'values/detail.html', {'value': value})