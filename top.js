<script>

(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({"./src/app.jsx":[function(require,module,exports){
var React = require('react');
var ReactDOM = require('react-dom');
var NavBar = require('./navBar');
var SearchSideBar = require('./searchSideBar');
var MainPain = require('./mainPane');


var App = React.createClass({displayName: "App",
  componentDidMount: function() {
    ReactDOM.findDOMNode(this)
    .offsetParent
    .addEventListener('keypress', function (e) {
      var intKey = (window.Event) ? e.which : e.keyCode;
      if (intKey > 47 && intKey < 58) {
        offset = 9;
        if(intKey != 48)
          offset = intKey - 49;
        list = document.getElementById("company-scrool-list");
        if(list)
        list.scrollLeft = 508 * offset;
      }
      else if(intKey == 45 || intKey == 61) {
        list = document.getElementById("company-scrool-list");
        if(list)
          list.scrollLeft = list.scrollLeft + (intKey == 45 ? -1 : 1) * 508;
      }
      else if(intKey == 96) {
        searchBox = document.getElementById("search-text-box");
        if(searchBox) {
          searchBox.select();
          searchBox.focus();
        }
      }
    }.bind(this));
  },
  updatePath: function(newPath) {
    this.setState({companyPath: newPath});
  },
  getInitialState: function() {
    return {
