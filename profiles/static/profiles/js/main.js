var validate;

var production = false;

if(production) {
	absurl = "http://172.31.48.144:8000/";
} else {
	absurl = "http://localhost:8000/";
}


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

	$('#payday-check').click(function(){
		saveValidate();
		savePayroll();
	});
	$('#send-comment').click(function(){
		saveComment()
	});
	$('#comment-Reload').click(function() {
		loadComments();
	});
	$('#week-reload').click(function() {
		loadWeek();
	})
	fillDates();

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
								'<option value="@">U</option>' +
							'</select></td>' +
						'</tr>';
	}
	return data_send;
}

//FIll the choosebox for weekview
function fillDates() {
	$.getJSON(absurl + "period/list/", function (data) {
		for(i = 0; i < data.length; i++) {
			$('#date-select').append('<option value' + data[i].fields.start_date + '>' + data[i].fields.start_date + '</option>');
		}
	});
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
		url: absurl +"payroll/paid/",
		data: send_data,
		dataType: "json",
		success: function (data) {
			var line = '';
			$.each(data, function(i, csr) {
				line += '<tr>' +
							'<td  class="payroll-user">'+ csr.payroll_number +'</td>' +
							'<td>' + csr.name + '</td>' +
							'<td>' + csr.schedule + '</td>' +
							'<td>' + Math.round(csr.paid_time * 100) / 100 + '</td>' +
							'<td>' + Math.round(csr.time_softphone *100) /100 + '</td>' +
							'<td>' + Math.round(csr.time_avaya * 100) / 100+ '</td>' +
							'<td>' + Math.round(csr.aux_paid *100) /100 +'</td>' +
							'<td style="font-weight: bold;">' + Math.round(csr.paid_total *100) /100 + '</td>';
				line += setAttrValue(csr.schedule, (Math.round(csr.paid_total *100) /100));
			});
			$("#payday-BodyTable").html(line);
			if(validateState() == true) {
				$('#payday-check').prop("disabled", true).html("Ready");
			}else {
				$('#payday-check').prop("disabled", false).html("Check");
			}
		}
		,fail: function(msg) {
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
		payroll_number = $father.children[x].children[0].innerHTML;
		name = $father.children[x].children[1].innerHTML;
		schedule = parseFloat($father.children[x].children[2].innerHTML);
		adjusted = parseFloat($father.children[x].children[3].innerHTML);
		softphone =  parseFloat($father.children[x].children[4].innerHTML);
		avaya =  parseFloat($father.children[x].children[5].innerHTML);
		aux =  parseFloat($father.children[x].children[6].innerHTML);
		paid_total =  parseFloat($father.children[x].children[7].innerHTML);
		status = $father.children[x].children[8].children[0].value;
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
		//console.log(send_data);

		$.ajax({
			type: "POST",
			url: absurl + "payroll/save/",
			data: send_data,
			dataType: "json",
			success: function (data) {
				console.log('Se enviaron con exitos los datos');

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
			url: absurl + "validate/status/",
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

function validateState() {
	return validatePayroll();
}

function saveValidate() {
	var date = moment($('.date-select').val().split("/").reverse().join("/")).format("YYYY-MM-DD");
	var send_data = {'day': date};
	var ret;
	ajaxSetup();
	$.ajax({
			type: "POST",
			url: absurl + "validate/save/",
			async: false,
			data: send_data,
			dataType: "json",
			success: function(data) {
				ret = data.status;
				$('#payday-check').prop('disabled', true).html("Ready");
				//console.log("Validate succes}");
			}
		});
	return ret;
}


function saveComment() {
	var date = moment($('.date-select').val().split("/").reverse().join("/")).format("YYYY-MM-DD");
	var $text = $('#comment-text').val()
	var send_data = {
		'day': date,
		'comment': $text
	};
	var ret;
	ajaxSetup();
	$.ajax({
			type: "POST",
			url: absurl + "comments/create/",
			async: false,
			data: send_data,
			dataType: "json",
			success: function(data) {
				$('.comment-content').hide();
				ret = data.success;
				alert(ret);
			}
		});
	return ret;
}

//AJAX to read comments
function loadComments() {
	ajaxSetup();
	var line = '';
	$.getJSON(absurl + "comments/list/", function (data) {
		console.log(data);
		$.each(data, function(i, csr) {
			console.log(csr);
			line += '<tr>' +
						'<td>' + csr.text + '</td>' +
						'<td>' + csr.user + '</td>' +
						'<td>' + csr.date + '</td>' +
						'<td><a href="' + absurl + 'comments/' + csr.id + '/">' + 'Validar' + '</a></td>' +
						'</tr>';
						console.log(line);
		});
		$('#comment-BodyTable').html(line);
	});
}

//AJAX for week view
function loadWeek() {
	var line = '';
	ajaxSetup();
	$.ajax({
		type: "POST",
		url: absurl + "payroll/week/list/",
		data: {'day': $('#date-select').val()},
		dataType: "json",
		success: function (data) {
			changeDate();
			for (var i = 0; i < data.length; i++) {
				console.log(i);
				if(!(data[i].length == 0)) {
					line += '<tr><td>' + 'id' +  '</td>' +
									'<td>' + data[i][0].name + '</td>' +
									'<td>28</td>'
									console.log(line);
					for (var j = 0; i < data.length; j++) {
						if(data[i][j] == undefined) break;
						line += '<td>' + data[i][j].paid_total + '</td>';
						console.log(data);
					}
					line += '</tr>';
				}

			}
			$('#week-bodytable').html(line);
		}
	});
}





window.onload = function() {
	var day = moment().isoWeekday(1);
	updateDate(day);
}
