var dias = 86400;


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

$(document).ready(function () {
	$('.date-select').datetimepicker({
		timepicker: false,
		format: 'd/m/Y'
	});
	$('.select-abbr').select2();
	$('#payday-Reload').click(changeDay());
});


function changeDay () {
	$.getJSON("http://localhost:8000/payroll/paid", function (data) {
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
					console.log(line);
		});
		$("#payday-BodyTable").html(line);
	});
}

window.onload = function() {
	var day = moment().isoWeekday(1);
	updateDate(day);
}
