import React, { useEffect, useState } from 'react';
import { getAllBLogs } from './services/Api';

const Blog=()=>{
    const[blogs,setBlogs]=useState([]);

    useEffect(()=>{
        getAllBLogs().then(response=>{
            console.log(response.data);
            setBlogs(response.data);
        }).catch(error=>{
            console.error("Error fetching blog",error);
        });
    },[]);

    return(
        <div>
            <h1>Blog List</h1>
            <ul>
                {blogs.map(blog=>(
                    <li key={blog.id}>
                        <h2>{blog.title}</h2>
                        <p>{blog.description}</p>
                        <p>{blog.category}</p>
                    </li>
                ))}
            </ul>
        </div>
    );


};

export default Blog;