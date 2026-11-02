/* STUB rig.js, written by the CEO so lint/snapshots work before the real rig lands.
 * The Character Designer overwrites this file with the real implementation (see production/RIG_API.md).
 * Every Rig.* call is a deterministic no-op that returns the timeline (or a harmless value),
 * so scenes written against the API never throw while the stub is in place. */
(function () {
  if (window.Rig && !window.Rig.__stub) return;
  var noop = function (tl) { return tl; };
  var known = {
    __stub: true,
    boil: noop,
    blink: noop,
    blinks: noop,
    lipSync: noop,
    lipsync: noop,
    mouth: noop,
    eyes: noop,
    look: noop,
    mood: noop,
    moods: noop,
    expression: noop,
    pose: noop,
    poses: noop,
    breathe: noop,
    idle: noop,
    walk: noop,
    hop: noop,
    squash: noop,
    take: noop,
    arm: noop,
    head: noop,
    init: function () { return null; },
    get: function () { return null; },
  };
  var handler = {
    get: function (target, prop) {
      if (prop in target) return target[prop];
      return noop;
    },
  };
  window.Rig = typeof Proxy === "function" ? new Proxy(known, handler) : known;
})();
