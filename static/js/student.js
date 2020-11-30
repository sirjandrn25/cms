


 const full_url = window.location.href;
 const path_name = window.location.pathname;
 const remaining_url = full_url.slice(full_url.indexOf(path_name),full_url.length-1);
 if ((remaining_url+"/") !== path_name){
   const arr = remaining_url.split('/');
   // console.log(remaining_url);
   const remaining_url_arr = arr[3].split('&');
   // console.log(remaining_url_arr);
   

   // this is for search value
   const search_arr = remaining_url_arr[1].split('=');
   let search_value = '';
   if (search_arr.length>1){
     const new_search_arr = search_arr[1].split('+');
     if (new_search_arr.length>1){
       search_value = new_search_arr[0]+' '+new_search_arr[1];
     }
     else{
       search_value=new_search_arr[0];
     }

   }
   const searh_field = document.getElementById('search_field');
   search_field.setAttribute('value',search_value)
   // this is for course selection 
   const course_arr = remaining_url_arr[0].split('=');

   const course_new_arr = course_arr[1].split('+');
   let course;
   if (course_new_arr.length>1){
     course = course_new_arr[0]+" "+course_new_arr[1];
   }
   else{
     course = course_new_arr[0];
   }
   let course_selection = document.getElementById('course_select');
   for(let c_opt of course_selection){
     if(c_opt.value === course){
       c_opt.setAttribute("selected",true);
       break;
     }
   }

 }
 let course_selection = document.getElementById('course_select');
 course_selection.onchange = function(){
   let form = document.getElementById('search_form');
   form.submit();
 }