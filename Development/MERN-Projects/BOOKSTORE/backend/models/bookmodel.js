import mongoose from 'mongoose';


const bookSchema = new mongoose.Schema(
    {
        title: {
            type: String,
            required: true
        },  
        author: {
            type: String,
            required: true
        },  
        publishYear: {
            type: Number,
            required: true
        }, 
        publisher: {
            type: String,
            required: true
        }
    } ,
    {   // This is an object that contains the configuration options for the schema}
    timestamps: true,
    }
    

);

export const Book = mongoose.model('Book', bookSchema );