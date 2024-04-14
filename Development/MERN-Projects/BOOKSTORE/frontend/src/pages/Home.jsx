import { useEffect, useState } from "react"
import React, {useEffect, useState} from 'react';
import axios from 'axios';
import Spinner from '../components/Spinner';
import { Link } from 'react-router-dom';
import {AiOutlineEdit} from 'react-icons/ai';
import {BsInfoCircle} from 'react-icons/bs';
import {MdOutlineAddBox} from 'react-icons/md';

const Home = () => {

  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(false);
  useEffect(() => {
    setLoading(true);
    axios.get('http://localhost:3000/api/book')
      .then(response => {
        setBooks(response.data.data);
        setLoading(false);
      })
      .catch(error => {
        setLoading(false);
      });

    //Stop at 32.43
  });

  return (
    <div>
      
    </div>
  )
}

export default Home
