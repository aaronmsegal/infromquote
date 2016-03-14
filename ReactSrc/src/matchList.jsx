var React = require('react');
var MatchListItem = require('./matchListItem')

module.exports = React.createClass({
  render: function() {
    return <div className="list-group">
      {this.renderList()}
    </div>
  },
  companyDisplayed: function (symbol) {
    for(i=0; i<this.props.companies.length; i++) {
      if(this.props.companies[i][2] == symbol) {
        return true;
      }
    }
    return false;
  },
  renderList: function() {
    if(!this.props.searchText ||
        this.props.searchText.length === 0 ||
        !this.props.searchItems) {
      return <h5 className="text-center">Enter company above.</h5>
    } else {
      var children = [];
      for(var key in this.props.searchItems) {
        var item=this.props.searchItems[key];
        item.key=key;
        name = item[1].toLowerCase();
        symbol = item[2].toLowerCase();
        if((symbol.indexOf(this.props.searchText.toLowerCase()) !== -1)
          || (name.toLowerCase().indexOf(this.props.searchText.toLowerCase()) !== -1)) {
          if( ! this.companyDisplayed(symbol)) {
            newPath = item[2] + "*" + this.props.companyPath + "&" + this.props.searchText;
            children.push(
              <MatchListItem
                name={item[1]}
                symbol={item[2]}
                key={key}
                path={newPath}
              />
            );
          }
        }
      }
      children.sort(this.sortChildren)
      return children;
    }
  },
  sortChildren: function(a, b) {
    if(a.props.name > b.props.name)
      return 1;
    return -1;
  }
});
