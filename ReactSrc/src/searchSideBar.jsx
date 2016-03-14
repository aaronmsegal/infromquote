var React = require('react');
var SearchBar = require('./searchBar');
var MatchList = require('./matchList')

module.exports = React.createClass({
  getInitialState: function() {
    return {
      searchText: this.props.searchText
    }
  },
  handleSearchChange: function(searchText) {
    if(searchText == "`") {
      this.resetSearch();
      return;
    }
    this.setState({searchText: searchText})
  },
  resetSearch: function() {
    this.setState({searchText: ""})
  },
  render: function() {
    return (
      <div className="col-sm-3 col-md-2 sidebar">
        <ul className="nav nav-sidebar">
          <SearchBar
            onInput={this.handleSearchChange}
            text={this.state.searchText}
          />
          <div className="text-center" >
            <a href="help">
              help
            </a>
          </div>
          <hr />
          <MatchList
            searchItems={this.props.searchItems}
            companies={this.props.companies}
            companyPath={this.props.companyPath}
            searchText={this.state.searchText}
          />
        </ul>
      </div>
    );
  }
});
