var React = require('react');

module.exports = React.createClass({
  render: function() {
    return (
        <div className="container-fluid">
          <div className="navbar-header">
            <a className="navbar-brand" href="#">
              {this.props.title}
            </a>
          </div>
        </div>
    );
  }
});
