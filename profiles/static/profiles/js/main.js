
$(document).ready(function () {
	$('.date-select').datetimepicker({
		timepicker: false,
		format: 'd/m/Y'
	});
	$('.select-abbr').select2();
	$('#payday-Reload').click(function (event) {
		event.preventDefault();
		changeDay();
	});
	
});


var csrftoken = $.cookie('csrftoken');

function updateDate(day) {
	$('#day1').html(day.format("DD/MM/YYYY"));
	$('#day2').html(day.add(1, 'd').format("DD/MM/YYYY"));
	$('#day3').html(day.add(1, 'd').format("DD/MM/YYYY"));
	$('#day4').html(day.add(1, 'd').format("DD/MM/YYYY"));
	$('#day5').html(day.add(1, 'd').format("DD/MM/YYYY"));
	$('#day6').html(day.add(1, 'd').format("DD/MM/YYYY"));
	$('#day7').html(day.add(1, 'd').format("DD/MM/YYYY"));
}

function changeDate() {
	var day = moment($('#date-select').val(), "YYYY-MM-DD");
	updateDate(day);
}


function changeDay () {
	console.log("Enter Daychange");
	var data_s = [];
	var date = moment($('.date-select').val().split("/").reverse().join("/")).format("YYYY-MM-DD");
	console.log(date);
	function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	function sameOrigin(url) {
	    // test that a given url is a same-origin URL
	    // url could be relative or scheme relative or absolute
	    var host = document.location.host; // host + port
	    var protocol = document.location.protocol;
	    var sr_origin = '//' + host;
	    var origin = protocol + sr_origin;
	    // Allow absolute or scheme relative URLs to same origin
	    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
	        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
	        // or any other URL that isn't scheme relative or absolute i.e relative.
	        !(/^(\/\/|http:|https:).*/.test(url));
	}
	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
	            // Send the token to same-origin, relative URLs only.
	            // Send the token only if the method warrants CSRF protection
	            // Using the CSRFToken value acquired earlier
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});
	var send_data = {'day': date};
	console.log(send_data);
	//data_s.push('{"day":' + date + '}');
	//data_s.push('{"csrfmiddlewaretoken":' + $.cookie("csrftoken") + '}');
	$.ajax({
		type: "POST",
		url: "http://localhost:8000/payroll/paid/", 
		data: send_data,
		//contentType: "application/json; charset=utf-8",
		dataType: "json",
		success: function (data) {
			console.log(data);
			var line = '';
			$.each(data, function(i, csr) {
				line += '<tr>' +
							'<td>250175</td>' +
							'<td>' + csr.name + '</td>' + 
							'<td>' + csr.schedule + '</td>' + 
							'<td>' + Math.round(csr.paid_time * 10) / 10 + '</td>' + 
							'<td>' + Math.round(csr.time_softphone *10) /10 + '</td>' +
							'<td>' + Math.round(csr.time_avaya * 10) / 10+ '</td>' +
							'<td>' + Math.round(csr.aux_paid *10) /10 +'</td>' +
							'<td style="font-weight: bold;">' + Math.round(csr.paid_total *10) /10 + '</td>' +
							'<td><select name="abbr" class="select-abbr">' +
								'<option value="W">W</option>' +
								'<option value="T">T</option>' +
								'<option value="R">R</option>' +
								'<option value="Z">Z</option>' +
								'<option value="H">H</option>' +
								'<option value="V">V</option>' +
								'<option value="O">O</option>'+
								'<option value="A">A</option>'+ 
								'<option value="I">I</option>' +
								'<option value="U">U</option>' +
							'</select></td>' +
						'</tr>';
			});
			$("#payday-BodyTable").html(line);
		},
		fail: function(msg) {
			console.log(msg);
		}
	});
	//alert("enter daychange");
}
/*
window.onload = function() {
	var day = moment().isoWeekday(1);
	updateDate(day);
}*/
