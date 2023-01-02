document.addEventListener("DOMContentLoaded", function () {
    $('td').on('click', function(){
        let clickId = $(this).attr('id')

        let auditorium = clickId.split('-')[0]
        let weekDay = clickId.split('-')[1]
        let lesson = clickId.split('-')[2]
        

        var selectWeekDay = document.getElementById("id_week_day");
        var options = selectWeekDay.options;
        for (var i = 0; i < options.length; i++) {

            if (options[i].value == weekDay) {
                selectWeekDay.value = options[i].value
                weekDayText = options[i].textContent
                }
            };


        var selectAuditorium = document.getElementById("id_auditorium");
        var options = selectAuditorium.options;
        for (var i = 0; i < options.length; i++) {

            if (options[i].textContent == auditorium) {
                selectAuditorium.value = options[i].value
                }
            };

        var selectClassTime = document.getElementById("id_class_time");
        var options = selectClassTime.options;
        for (var i = 0; i < options.length; i++) {

            if (options[i].textContent == lesson) {
                selectClassTime.value = options[i].value
                }
            };
        var labels = document.getElementsByTagName('label')
        var labelWeekDay = labels[1]
        labelWeekDay.innerText = 'День недели: ' + weekDayText

        var labelLesson = labels[2]
        labelLesson.innerText = 'Номер урока: ' + lesson

        var labelAuditorium = labels[3]
        labelAuditorium.innerText = 'Номер аудитории: ' + auditorium
        
     });

    var select = document.getElementById("grouping_select");     
    // var input = document.querySelector("input");
    
    select.addEventListener("change", function(){
        console.log('adasdasdad')
        var selectValue = this.options[this.selectedIndex].text;
        // console.log(this.options[this.selectedIndex].text)
        cells = document.getElementsByClassName('color_hover')
        // console.log(cells)
        for (let i = 0; i < cells.length; i += 1) {
            // Этот код выполняется для каждого элемента
            console.log(cells[i].innerText);
            if (cells[i].innerText === selectValue) {
                cells[i].style.backgroundColor = '#aab2bd';
            } else {
                cells[i].style.backgroundColor = '#ffffff';
            }
        }
    });
    
})

