
// ************* start for course and subject selection *********

const course = document.getElementById('id_course');
const subject = document.getElementById('id_subject');



const remove_options = (selectBox)=>{
    const length = selectBox.options.length;
    for(let i=length-1; i>=0; i--){
        selectBox.options[i]=null;
    }

}

const add_options = (selectBox,items)=>{
    let i = 0;
    // console.log(items);
    
    for(let item of items ){
        let option = document.createElement('option');
        option.setAttribute('value',item.id);
        option.innerHTML=item.name;
        selectBox.add(option);
        
    }
    
}

const fetch_subjects = (course_id)=>{
    const url = `/college/attendance_management/get_subjects/${course_id}/`;
    fetch(url).then(response=>response.json()).then(json_data=>{
        remove_options(subject);
        add_options(subject,json_data.subjects);
        
    }).catch(error=>{
        console.log(error)
    })
}





const attendance_list=document.getElementById('attendance_list');
if(attendance_list){
    
}
else{
    fetch_subjects(course.options[0].value);
}


course.addEventListener('change',(e)=>{
    fetch_subjects(e.target.value);
    
})

// ************* start for course and subject selection *********




// ************* this is all for student attendanced check box********
const all_check = document.getElementById('all_check');
const student_checks = document.querySelectorAll('.student_check');
// console.log(student_checks);





const check_attendance = ()=>{
    let flag = true;
    for(let check_node of student_checks){
        if(check_node.checked){
            continue;
        }
        else{
            flag=false;
        }
    }
    if(flag){
        all_check.setAttribute('checked',true);
    }
    else{
        all_check.removeAttribute('checked');
    }
}

window.onload = check_attendance();

for(let check_node of student_checks){
    check_node.addEventListener('change',()=>{
        check_attendance();
    })
}

all_check.addEventListener('change',()=>{
    if(all_check.checked){
        for(let check_node of student_checks){
            check_node.setAttribute('checked',true);
        }
    }
    else{
        for(let check_node of student_checks){
            check_node.removeAttribute('checked');
        }
    }
})