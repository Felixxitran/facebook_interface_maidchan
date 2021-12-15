'use strict';
const express = require('express'),
const bodyParser = require('body-parser'),
const app = express().use(bodyParser.json());


app.listen(process.env.PORT ||1337 ,()=>console.log('webhook is listening'))