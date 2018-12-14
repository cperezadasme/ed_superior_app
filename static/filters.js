function set_data_endpoint(endpoint, form_name){
	$.ajax({
		url: endpoint,
		type: 'GET',
	}).done(function (data) {
		console.log('done')
		for (var row of data) {
	    	console.log(row);
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
        query_param: 'institution',
    },
    'area': {
        endpoint: '/api/area-knowledge/',
        query_param: 'area',
    },
};

for (var param in params) {
	console.log('param', param)
	var endpoint = params[param].endpoint;
	console.log('endpoint', endpoint)
	var form_name = '#form__' + param;
	console.log('form_name', form_name);

	set_data_endpoint(endpoint, form_name);
}
