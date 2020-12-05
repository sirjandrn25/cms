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
        // console.log(json_data.subjects)
        remove_options(subject);
        add_options(subject,json_data.subjects);
        
    }).catch(error=>{
        console.log(error)
    })
}

course.addEventListener("change",e=>{
    fetch_subjects(e.target.value)
})
// window.onload = fetch_subjects()
window.onload=fetch_subjects(course.options[0].value)