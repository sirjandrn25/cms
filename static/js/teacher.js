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


const search_form = document.getElementById('search_form');
const course_option = document.getElementById('select_course');
course_option.addEventListener("change",e=>{
    search_form.submit()
})



window.onload=fetch_subjects(course.options[0].value)


const full_url = window.location.href;
const path_name = window.location.pathname;
const remaining_url = full_url.slice(full_url.indexOf(path_name),full_url.length-1);
const index = remaining_url.indexOf("?");

const course_option_map = ()=>{
    const search_value = remaining_url.substr(index+1,remaining_url.length);
    const course_search = (search_value.split('&'))[0];
    const course_value = (course_search.split('='))[1]

    for(let option of course_option){
        if(option.value === course_value){
            option.setAttribute('selected',true);
            break;
        }
    }
}
if (index !=-1){
    
    window.onload = course_option_map();
}
    





