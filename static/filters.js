function set_data_endpoint(endpoint, form_name){
	$.ajax({
		url: endpoint,
		type: 'GET',
	}).done(function (data) {
		for (var row of data) {
	        $(form_name).append(
	            '<option value="' + row+ '">' + row + '</option>'
	        );
	    }
	});
};

var params = {
    'year': {
        endpoint: '/api/years/',
        query_param: 'year',
    },
    'institution': {
        endpoint: '/api/instituion-classification-3/',
        query_param: 'institution_classification_level_3',
    },
    'area': {
        endpoint: '/api/area-knowledge/',
        query_param: 'area_of_knowledge',
    },
};

for (var param in params) {
	var endpoint = params[param].endpoint;
	var form_name = '#form__' + param;

	set_data_endpoint(endpoint, form_name);
}

var get_filter_data = function() {
        var query_params = {};
        for (var param in params) {
			var form_name = '#form__' + param;

			if ($(form_name).val() != 'all') {
				var key = params[param].query_param;
				query_params[key] = $(form_name).val();	
			}

		}

        return query_params;

    };

var multiline = function () {
	query_params = get_filter_data();
	$('#multiline').empty();
	render_multiline(query_params);
}

var barchart = function(){
	query_params = get_filter_data();
	query = '?'

	console.log(query_params)
	if (query_params.hasOwnProperty('year')){
		console.log('year')
		query += 'year=' + query_params.year;
	}
	if (query_params.hasOwnProperty('area_of_knowledge')){
		console.log('area_of_knowledge')
		query += 'area_of_knowledge=' + query_params.area_of_knowledge;
	}
	if (query_params.hasOwnProperty('institution_classification_level_3')){
		console.log('institution_classification_level_3')
		query += 'institution_classification_level_3=' + query_params.institution_classification_level_3;
	}
	console.log(query)
	render_barchart(query);
}

var render = function () {
	multiline();
	barchart();
}

$('#form__btn').on('click', render);
