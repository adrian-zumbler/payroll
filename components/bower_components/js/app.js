
$('#menu-toggle').click(function() {
    $('.ui.sidebar').sidebar('toggle');
});

var content =  get_all_agents();

function get_all_agents() {
  var agents;
  var data = []
  $.ajax({
    url:"http://localhost:8000/agents/all/",
    success: function(data) {
      agents = data;
    },async:false
  });
  agents = JSON.parse(agents);
  for(i=0;i<agents.length;i++){data.push({title: agents[i].fields.first_name +" "+  agents[i].fields.last_name })}
  return data;
}

$('.ui.dropdown').dropdown();

$('.ui.search')
  .search({
    source: content
  });

$('#txtDate-do').datetimepicker({
  		timepicker: false,
  		format: 'Y-m-d'
  	});

$('#txtDate-finish').datetimepicker({
      		timepicker: false,
      		format: 'Y-m-d'
});

$('#txtStart').datetimepicker({
          datepicker:false,
      		timepicker: true,
      		format: 'H:m'
});
$('#txtEnd').datetimepicker({
          datepicker:false,
      		timepicker: true,
      		format: 'H:m'
});

$('#dateSearch').datetimepicker({
          datepicker:true,
      		timepicker: false,
      		format: 'Y-m-d'
});

$('#slcActivity').change(function() {
  idActivity = $('#slcActivity').val();
  //Evalua si una actividad es una resticción por un id
  if (idActivity == 10) {
    $('.restrictionContainer').fadeToggle();
  } else {
    $('.restrictionContainer').fadeOut();
  }
});


$('.ui.toggle.checkbox').checkbox().first().checkbox({
  onChange: function() {
    $('#startEndBlock').fadeToggle()
  }
});
