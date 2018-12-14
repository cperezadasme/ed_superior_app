function get_max(data) {
	var max = 0;
	data.forEach(function(d){
		var aux_max = d3.max(d.values, d => d.total);
		if (aux_max > max){
			max = aux_max;
		};
	});

	return max;
};

$.ajax({
	url: '/api/total-graduates',
	type: "GET",
}).done(function(data){
	var margin_top = 20, margin_right=20, margin_bottom=50, margin_left=70

	var width = 960 - margin_left - margin_right;
	var height = 500  - margin_top - margin_bottom;
	var margin = 50;
	var duration = 250;

	var lineOpacity = "0.25";
	var lineOpacityHover = "0.85";
	var otherLinesOpacityHover = "0.1";
	var lineStroke = "1.5px";
	var lineStrokeHover = "2.5px";

	var circleOpacity = '0.85';
	var circleOpacityOnLineHover = "0.25"
	var circleRadius = 3;
	var circleRadiusHover = 6;


	/* Format Data */
	var parseDate = d3.timeParse("%Y");
	data.forEach(function(d) { 
	  d.values.forEach(function(d) {
	    d.year = parseDate(d.year);
	    d.total = +d.total;    
	  });
	});

	/* Scale */
	var xScale = d3.scaleTime()
	  .domain(d3.extent(data[0].values, d => d.year))
	  .range([0, width-margin]);

	var yScale = d3.scaleLinear()
	  .domain([0, get_max(data) + 10000])
	  .range([height-margin, 0]);

	var color = d3.scaleOrdinal(d3.schemeCategory10);

	/* Add SVG */
	var svg = d3.select("#multiline").append("svg")
	  .attr("width", (width+margin)+"px")
	  .attr("height", (height+margin)+"px")
	  .append('g')
	  .attr("transform", `translate(${margin}, ${margin})`);


	/* Add line into SVG */
	var line = d3.line()
	  .x(d => xScale(d.year))
	  .y(d => yScale(d.total));

	let lines = svg.append('g')
	  .attr('class', 'lines');

	lines.selectAll('.line-group')
	  .data(data).enter()
	  .append('g')
	  .attr('class', 'line-group')  
	  .on("mouseover", function(d, i) {
	      svg.append("text")
	        .attr("class", "title-text")
	        .style("fill", color(i))        
	        .text(d.name)
	        .attr("text-anchor", "middle")
	        .attr("x", (width-margin)/2)
	        .attr("y", 5);
	    })
	  .on("mouseout", function(d) {
	      svg.select(".title-text").remove();
	    })
	  .append('path')
	  .attr('class', 'line')  
	  .attr('d', d => line(d.values))
	  .style('stroke', (d, i) => color(i))
	  .style('opacity', lineOpacity)
	  .on("mouseover", function(d) {
	      d3.selectAll('.line')
						.style('opacity', otherLinesOpacityHover);
	      d3.selectAll('.circle')
						.style('opacity', circleOpacityOnLineHover);
	      d3.select(this)
	        .style('opacity', lineOpacityHover)
	        .style("stroke-width", lineStrokeHover)
	        .style("cursor", "pointer");
	    })
	  .on("mouseout", function(d) {
	      d3.selectAll(".line")
						.style('opacity', lineOpacity);
	      d3.selectAll('.circle')
						.style('opacity', circleOpacity);
	      d3.select(this)
	        .style("stroke-width", lineStroke)
	        .style("cursor", "none");
	    });


	/* Add circles in the line */
	lines.selectAll("circle-group")
	  .data(data).enter()
	  .append("g")
	  .style("fill", (d, i) => color(i))
	  .selectAll("circle")
	  .data(d => d.values).enter()
	  .append("g")
	  .attr("class", "circle")  
	  .on("mouseover", function(d) {
	      d3.select(this)     
	        .style("cursor", "pointer")
	        .append("text")
	        .attr("class", "text")
	        .text(`${d.total}`)
	        .attr("x", d => xScale(d.year) + 5)
	        .attr("y", d => yScale(d.total) - 10);
	    })
	  .on("mouseout", function(d) {
	      d3.select(this)
	        .style("cursor", "none")  
	        .transition()
	        .duration(duration)
	        .selectAll(".text").remove();
	    })
	  .append("circle")
	  .attr("cx", d => xScale(d.year))
	  .attr("cy", d => yScale(d.total))
	  .attr("r", circleRadius)
	  .style('opacity', circleOpacity)
	  .on("mouseover", function(d) {
	        d3.select(this)
	          .transition()
	          .duration(duration)
	          .attr("r", circleRadiusHover);
	      })
	    .on("mouseout", function(d) {
	        d3.select(this) 
	          .transition()
	          .duration(duration)
	          .attr("r", circleRadius);  
	      });


	/* Add Axis into SVG */
	var xAxis = d3.axisBottom(xScale).ticks(5);
	var yAxis = d3.axisLeft(yScale).ticks(5);

	// Add the x Axis
	svg.append("g")
	  .attr("transform", `translate(0, ${height-margin})`)
	  .call(xAxis);

	// text label for the x axis
	svg.append("text")             
	  .attr("transform",
	        "translate(" + (width/2) + " ," + 
	                       (height + margin_top + 20) + ")")
	  .style("text-anchor", "middle")
	  .text("Date");

	// Add the y Axis
	svg.append("g")
	  .call(yAxis);

	// text label for the y axis
	svg.append("text")
	  .attr("transform", "rotate(-90)")
	  .attr("y", 0 - margin_left)
	  .attr("x",0 - (height / 2))
	  .attr("dy", "1em")
	  .style("text-anchor", "middle")
	  .text("Value"); 

	svg.append("g")
	  .attr("class", "x axis")
	  .attr("transform", `translate(0, ${height-margin})`)
	  .call(xAxis);

	svg.append("g")
	  .attr("class", "y axis")
	  .call(yAxis)
	  .append('text')
	  .attr("y", 15)
	  .attr("transform", "rotate(-90)")
	  .attr("fill", "#000")
	  .text("Total Titulados");
});
