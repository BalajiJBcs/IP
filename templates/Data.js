// Array of events
var events_array = [{
		title: "Shift 1",
		// Set to 1st of the month at 12:00 am
		start: moment("2018-04-15 11:30"),
		 // Set to en the 1st of the month at 1:30 am
		 end: moment("2018-04-15 11:30").add(4, 'hours'),
		 color: "#D44500"
		 }, {
		 title: "Shift 2",
		 // Set to 1st of the month at 12:00 am
		 start: moment("2018-04-18 16:30"),
		 // Set to end the 1st of the month at 3:00 am
		 end: moment("2018-04-18 19:00"),
		 color: "#D44500"
		 }, {
		 title: "Shift 3",
		 // Set to start the 1st of the month
		 start: moment("2018-04-21 19:00"),
		 // Set to end one week after the start of the month
		 end: moment("2018-04-21 23:00"),
		 color: "#D44500"
		 },
		 {
		title: "Shift 4",
		// Set to 1st of the month at 12:00 am
		start: moment("2018-04-21 11:30"),
		 // Set to en the 1st of the month at 1:30 am
		 end: moment("2018-04-21 11:30").add(4, 'hours'),
		 color: "#D44500"
		 },
		 {
		title: "Shift 5",
		// Set to 1st of the month at 12:00 am
		start: moment("2018-04-22 11:30"),
		 // Set to en the 1st of the month at 1:30 am
		 end: moment("2018-04-22 11:30").add(4, 'hours'),
		 color: "#D44500"
		 },
		 {
		title: "Shift 12",
		// Set to 1st of the month at 12:00 am
		start: moment("2018-04-23 11:30"),
		 // Set to en the 1st of the month at 1:30 am
		 end: moment("2018-04-23 11:30").add(4, 'hours'),
		 color: "#D44500"
		 }
 ];
 
 
 
 // Array of events
var availableShifts_array = [{
		 title: "Shift 1",
		// Set to 1st of the month at 12:00 am
		 start: moment("2018-04-17 11:30"),
		 // Set to en the 1st of the month at 1:30 am
		 end: moment("2018-04-17 11:30").add(4, 'hours'),
		 color: "#009900",
		 author : "ABC"
		 }, {
		 title: "Shift 2",
		 // Set to 1st of the month at 12:00 am
		 start: moment("2018-04-18 16:30"),
		 // Set to end the 1st of the month at 3:00 am
		 end: moment("2018-04-18 19:00"),
		 color: "#009900",
		 author : "DEF"
		 }, {
		 title: "Shift 3",
		 // Set to start the 1st of the month
		 start: moment("2018-04-21 19:00"),
		 // Set to end one week after the start of the month
		 end: moment("2018-04-21 23:00"),
		 color: "#009900",
		 author : "Anuja Mahajan"
		 },
		 {
		 title: "Shift 4",
		 // Set to 1st of the month at 12:00 am
		 start: moment("2018-04-18 16:30"),
		 // Set to end the 1st of the month at 3:00 am
		 end: moment("2018-04-18 19:00"),
		 color: "#009900",
		 author : "ssdkfhs"
		 },
		 {
		 title: "Shift 5",
		 // Set to 1st of the month at 12:00 am
		 start: moment("2018-04-18 16:30"),
		 // Set to end the 1st of the month at 3:00 am
		 end: moment("2018-04-18 19:00"),
		 color: "#009900",
		 author : "ferferfer"
		 },
		 {
		 title: "Shift 5",
		 // Set to 1st of the month at 12:00 am
		 start: moment("2018-04-18 16:30"),
		 // Set to end the 1st of the month at 3:00 am
		 end: moment("2018-04-18 19:00"),
		 color: "#009900",
		 author : "ferferfer"
		 },
		 {
		 title: "Shift 5",
		 // Set to 1st of the month at 12:00 am
		 start: moment("2018-04-18 16:30"),
		 // Set to end the 1st of the month at 3:00 am
		 end: moment("2018-04-18 19:00"),
		 color: "#009900",
		 author : "ferferfer"
		 },
		 {
		 title: "Shift 5",
		 // Set to 1st of the month at 12:00 am
		 start: moment("2018-04-18 16:30"),
		 // Set to end the 1st of the month at 3:00 am
		 end: moment("2018-04-18 19:00"),
		 color: "#009900",
		 author : "rgrtgrtgrgrtgrtg"
		 }
 ];
 
 var chartData = [
					{
						value: 15,
						color: "#D44500",
						highlight: "#B33C00",
						label:"Worked Hours"						
					},				
					{
						value: 5,
						color: "#000066",
						highlight: "Gray",
						label: "Hours Remaining"						
					}
];