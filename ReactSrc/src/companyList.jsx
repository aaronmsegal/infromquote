var React = require('react');
var CompanyPane = require('./companyPane')

module.exports = React.createClass({
  // getInitialState: function() {
  //   return {
  //     companies: this.props.companies
  //   };
  // },
  toStart: function(oldIndex) {
    if(oldIndex == 0)
      return;
    newcompanies = [];
    newcompanies.push(this.props.companies[oldIndex])
    for(i = 0; i < this.props.companies.length; i++) {
      if(i != oldIndex)
        newcompanies.push(this.props.companies[i]);
    }
    //this.setState({companies: newcompanies});
    this.props.updateCompanies(newcompanies)
  },
  toBack: function(oldIndex) {
    if(oldIndex == this.props.companies.length-1)
      return;
    newcompanies = [];
    for(i = 0; i < this.props.companies.length; i++) {
      if(i != oldIndex)
        newcompanies.push(this.props.companies[i]);
    }
    newcompanies.push(this.props.companies[oldIndex]);
    //this.setState({companies: newcompanies});
    this.props.updateCompanies(newcompanies)
  },
  toLeft: function(oldIndex) {
    if(oldIndex == 0)
      return;
    newIndex = oldIndex - 1;
    newcompanies = [];
    for(i = 0; i < this.props.companies.length; i++) {
      if(i == newIndex) {
        newcompanies.push(this.props.companies[oldIndex]);
        newcompanies.push(this.props.companies[oldIndex-1]);
      }
      else if(i != oldIndex)
        newcompanies.push(this.props.companies[i]);
    }
    //this.setState({companies: newcompanies});
    this.props.updateCompanies(newcompanies)
  },
  toRight: function(oldIndex) {
    if(oldIndex == this.props.companies.length -1)
      return;
    newIndex = oldIndex + 1;
    newcompanies = [];
    for(i = 0; i < this.props.companies.length; i++) {
      if(i == newIndex) {
        newcompanies.push(this.props.companies[oldIndex+1]);
        newcompanies.push(this.props.companies[oldIndex]);
      }
      else if(i != oldIndex)
        newcompanies.push(this.props.companies[i]);
    }
    //this.setState({companies: newcompanies});
    this.props.updateCompanies(newcompanies)
  },
  render: function() {
    children = [];
    index = 0;
    for(i = 0; i < this.props.companies.length; i++) {
      children.push(
        <CompanyPane
          key={i}
          index={i}
          company={this.props.companies[i]}
          toLeft={this.toLeft}
          toRight={this.toRight}
          toBack={this.toBack}
          toStart={this.toStart}
        />
      );
      index++;
    }
    return (
      <div className="row-fluid">
        {children}
      </div>
    );
  }
});
