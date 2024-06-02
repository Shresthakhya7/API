import axios from 'axios';


const API_URL='http://127.0.0.1:8000/';


const api=axios.create({
    baseURL: API_URL,
});


export const getAllBLogs =() =>{
    return api.get('/blogs/');
};
export const getBlogById =(id) =>{
    return api.get(`/blogs/${id}/`);
};

export const postBlogs =(blogData) =>{
    return api.post('/post/',blogData);
};

export const updateBlogs =(id, blogData) =>{
    return api.put(`/update/${id}/`,blogData);
};

export default api;


