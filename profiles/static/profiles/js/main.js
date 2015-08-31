var validate;

$(document).ready(function () {
	$('.date-select').datetimepicker({
		timepicker: false,
		format: 'd/m/Y'
	});
	$('.select-abbr').select2();
	$('.menu').dropit();
	$('#payday-Reload').click(function (event) {
		event.preventDefault();
		changeDay();
	});
	$('#comment-button').click(function(){
		$('.comment-content').toggle();
	});
	$('#checkpay').click(function(){
		savePayroll();
	});

});

//var csrftoken = $.cookie('csrftoken');
//Update date in week view
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

//CSRFToken for ajax requests
function ajaxSetup() {
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
	            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
	        }
	    }
	});
}

//Set the attribute value for the csr in day view
function setAttrValue(scheduled, paid) {
	var data_send = "";
	if(scheduled > 0) {
		if(paid == 0) {
			data_send = '<td><select name="abbr" class="select-abbr">' +
								'<option value="W">W</option>' +
								'<option value="T">T</option>' +
								'<option value="R">R</option>' +
								'<option value="Z">Z</option>' +
								'<option value="H">H</option>' +
								'<option value="V">V</option>' +
								'<option value="O">O</option>'+
								'<option class="selected" selected value="A">A</option>'+
								'<option value="I">I</option>' +
								'<option value="U">U</option>' +
							'</select></td>' +
						'</tr>';
		} else {
			data_send = '<td><select name="abbr" class="select-abbr">' +
								'<option class="selected value="W">W</option>' +
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
		}
	} else if (scheduled == 0) {
		data_send = '<td><select name="abbr" class="select-abbr">' +
								'<option value="W">W</option>' +
								'<option value="T">T</option>' +
								'<option class="selected" selected value="R">R</option>' +
								'<option value="Z">Z</option>' +
								'<option value="H">H</option>' +
								'<option value="V">V</option>' +
								'<option value="O">O</option>'+
								'<option value="A">A</option>'+
								'<option value="I">I</option>' +
								'<option value="U">U</option>' +
							'</select></td>' +
						'</tr>';
	}
	return data_send;
}



/*AJAX Request*/
//Ajax request for the day view
function changeDay () {
	var data_s = [];
	var date = moment($('.date-select').val().split("/").reverse().join("/")).format("YYYY-MM-DD");
	var send_data = {'day': date};
	ajaxSetup();
	$.ajax({
		type: "POST",
		url: "http://localhost:8000/payroll/paid/",
		data: send_data,
		dataType: "json",
		success: function (data) {
			var line = '';
			$.each(data, function(i, csr) {
				line += '<tr>' +
							'<td  class="payroll-user">'+ csr.payroll_number +'</td>' +
							'<td>' + csr.name + '</td>' +
							'<td>' + csr.schedule + '</td>' +
							'<td>' + Math.round(csr.paid_time * 10) / 10 + '</td>' +
							'<td>' + Math.round(csr.time_softphone *10) /10 + '</td>' +
							'<td>' + Math.round(csr.time_avaya * 10) / 10+ '</td>' +
							'<td>' + Math.round(csr.aux_paid *10) /10 +'</td>' +
							'<td style="font-weight: bold;">' + Math.round(csr.paid_total *10) /10 + '</td>';
				line += setAttrValue(csr.schedule, (Math.round(csr.paid_total *10) /10));
			});
			$("#payday-BodyTable").html(line);
		},
		fail: function(msg) {
			console.log(msg);
		}
	});
}

//AJAX request for the supervisor to check the day to ok
function savePayroll() {
	$father = document.getElementById('payday-BodyTable');
	var date = moment($('.date-select').val().split("/").reverse().join("/")).format("YYYY-MM-DD");
	var payroll_number;
	var name;
	var schedule;
	var adjusted;
	var softphone;
	var avaya;
	var aux;
	var paid_total;
	var status;
	ajaxSetup();
	for(x = 0; x < $father.children.length;x++){
		payroll_number = $father.children[x].children[0].innerText;
		name = $father.children[x].children[1].innerText;
		schedule = parseFloat($father.children[x].children[2].innerText);
		adjusted = parseFloat($father.children[x].children[3].innerText);
		softphone =  parseFloat($father.children[x].children[4].innerText);
		avaya =  parseFloat($father.children[x].children[5].innerText);
		aux =  parseFloat($father.children[x].children[6].innerText);
		paid_total =  parseFloat($father.children[x].children[7].innerText);
		status = $father.children[x].children[8].children[0].getElementsByClassName('selected')[0].value;
		var send_data = {
			'day' : date,
			'payroll_number': payroll_number,
			'name': name,
			'schedule':schedule,
			'adjusted': adjusted,
			'softphone':softphone,
			'avaya': avaya,
			'aux': aux,
			'paid_total': paid_total,
			'status': status
		}
		$.ajax({
			type: "POST",
			url: "http://localhost:8000/payroll/save/",
			data: send_data,
			dataType: "json",
			success: function (data) {
				console.log('Se enviaron con exitos los datos')
			},
			fail: function(msg) {
				console.log(msg);
			}
		});

	}
}



function validatePayroll(){
	var date = moment($('.date-select').val().split("/").reverse().join("/")).format("YYYY-MM-DD");
	var send_data = {'day': date};
	var ret;
	ajaxSetup();
	$.ajax({
			type: "POST",
			url: "http://localhost:8000/validate/",
			async: false,
			data: send_data,
			dataType: "json",
			success: function(data) {
				ret = data.exist;
				//console.log(ret);
			}
		});
	return ret;
}

function test() {
	return validatePayroll();
}


/*
function validateState() {
	var s;
	validatePayroll(function(output){
		console.log(output);
		s = output;
	});
	return s;
}
*/

window.onload = function() {
	var day = moment().isoWeekday(1);
	updateDate(day);
}
