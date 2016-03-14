var React = require('react');
var CompanyList = require('./companyList');
var ScrollList = require('./scrollList');

module.exports = React.createClass({
  getInitialState: function() {
    return {
      companies: this.props.companies,
      target: 0
    };
  },
  updateCompanies: function(newcompanies) {
    // var newPath = "";
    // newcompanies.forEach {
    //   newpath += company.symbol + "*";
    // }
    this.setState({companies: newcompanies});
  },
  render: function() {
    return (
      <div className="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
        <div className="span1 container" id="company-scrool-list">
          <CompanyList
            companies={this.state.companies}
            updateCompanies={this.updateCompanies}
          />
        </div>
        <nav className="span2">
          <ScrollList
            companies={this.state.companies}
          />
        </nav>
      </div>
    );
  }
});
