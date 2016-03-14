var React = require('react');

module.exports = React.createClass({
  displayYearlies: function(ys) {
    lines =[];
    for(i = 0; i < ys.length; i++) {
      lines.push (
        <div key={i}>
          <h5>{ys[i][0]}  :  {ys[i][1]}</h5>
        </div>
      );
    }
    return lines;
  },
  handleLeft: function() {
    this.props.toLeft(this.props.index);
  },
  handleRight: function() {
    this.props.toRight(this.props.index);
  },
  handleStart: function() {
    this.props.toStart(this.props.index);
  },
  handleBack: function() {
    this.props.toBack(this.props.index);
  },
  render: function() {
    name = this.props.company[1]
    symbol = this.props.company[2]
    googleFinanceLink = "https://www.google.com/finance?q=" + symbol
    city = this.props.company[3]
    state = this.props.company[4]
    desc = this.props.company[5]
    ceo = this.props.company[6]
    website = this.props.company[7]
    yearlies = this.props.company[8]

    return (
      <div className="row panel company">

        <div className="btn-group" role="group">
          <button type="button"
            className="btn btn-default ctrbutton"
            aria-label="Left Align"
            onClick={this.handleStart}
            data-toggle="tooltip"
            title="Send to Front">
            <span className="glyphicon glyphicon-fast-backward" aria-hidden="true"></span>
          </button>
          <button type="button"
            className="btn btn-default ctrbutton"
            aria-label="Left Align"
            onClick={this.handleLeft}
            data-toggle="tooltip"
            title="Send to Left">
            <span className="glyphicon glyphicon-triangle-left" aria-hidden="true"></span>
          </button>
          <button type="button"
            className="btn btn-default ctrbutton"
            aria-label="Left Align"
            onClick={this.handleRight}
            data-toggle="tooltip"
            title="Send to Right">
            <span className="glyphicon glyphicon-triangle-right" aria-hidden="true"></span>
          </button>
          <button type="button"
            className="btn btn-default ctrbutton"
            aria-label="Left Align"
            onClick={this.handleBack}
            data-toggle="tooltip"
            title="Send to End">
            <span className="glyphicon glyphicon-fast-forward" aria-hidden="true"></span>
          </button>
        </div>

        <h1>
          {name}
          <span className="span4">   </span>
          <a target="_blank" href={googleFinanceLink}>
            <button type="button"
              className="btn btn-primary"
              data-toggle="tooltip"
              title="View Charts">
              <h4> {symbol.toUpperCase()} </h4>
            </button>
          </a>
        </h1>
        <hr />
        <a target="_blank" href={website}>
          <h4>{website}</h4>
        </a>
        <h4>CEO:  {ceo}</h4>
        <h5>Headquarters:  {city},  {state}</h5>
        <hr />
        {this.displayYearlies(yearlies)}
      </div>
    );
  }
});
