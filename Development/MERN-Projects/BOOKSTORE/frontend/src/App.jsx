import React from 'react'
import { Routes, Route } from 'react-router-dom'
import CreateBook from './pages/CreateBook'
import DeleteBook from './pages/DeleteBook'
import EditBook from './pages/EditBook' 
import Home from './pages/Home'
import ShowBook from './pages/ShowBook'

const App = () => {
  return (
    <Routes>
      <Route path='/' component={<Home/>} />
      <Route path='/create' component={<CreateBook/>} />
      <Route path='/edit/:id' component={<EditBook/>} />
      <Route path='/delete/:id' component={<DeleteBook/>} />
      <Route path='/show/:id' component={<ShowBook/>} />
    </Routes>
  )
}

export default App
