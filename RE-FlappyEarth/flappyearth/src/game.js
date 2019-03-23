(function() {

    window.onload = function() {
        game.init();
    }

    var game = window.game = {
        width: 0,
        height: 0,
        craso_x: 0,

        asset: null,
        stage: null,
        ticker: null,
        state: null,
        score: 0,

        bg: null,
        ground: null,
        bird: null,
        holdbacks: null,
        gameReadyScene: null,
        gameOverScene: null,
        flag: "",
        data: "\x2b\x58\x41\x05\x12\x55\x40\x08\x12\x44\x66\x09\x11\x68\x00\x0a\x5f\x49\x58\x01\x39\x52\x0a\x07\x6c\x10\x47\x05\x55\x4c\x5c\x15",

        init: function() {
            this.asset = new game.Asset();
            this.asset.on('complete', function(e) {
                this.asset.off('complete');
                this.initStage();
            }.bind(this));
            this.asset.load();
        },

        initStage: function() {
            this.width = Math.min(innerWidth, 450) * 2;
            this.height = Math.min(innerHeight, 750) * 2;
            this.scale = 0.5;

            //舞台画布
            var renderType = location.search.indexOf('dom') != -1 ? 'dom' : 'canvas';

            //舞台
            this.stage = new Hilo.Stage({
                renderType: renderType,
                width: this.width,
                height: this.height,
                scaleX: this.scale,
                scaleY: this.scale
            });
            document.body.appendChild(this.stage.canvas);

            //启动计时器
            this.ticker = new Hilo.Ticker(60);
            this.ticker.addTick(Hilo.Tween);
            this.ticker.addTick(this.stage);
            this.ticker.start(true);

            //绑定交互事件
            this.stage.enableDOMEvent(Hilo.event.POINTER_START, true);
            this.stage.on(Hilo.event.POINTER_START, this.onUserInput.bind(this));

            //Space键控制
            if (document.addEventListener) {
                document.addEventListener('keydown', function(e) {
                    if (e.keyCode === 32) this.onUserInput(e);
                }.bind(this));
            } else {
                document.attachEvent('onkeydown', function(e) {
                    if (e.keyCode === 32) this.onUserInput(e);
                }.bind(this));
            }

            //舞台更新
            this.stage.onUpdate = this.onUpdate.bind(this);

            //初始化
            this.initBackground();
            this.initScenes();
            this.initHoldbacks();
            this.initBird();
            this.initCurrentScore();

            //准备游戏
            this.gameReady();
        },

        initBackground: function() {
            //背景
            var bgWidth = this.width * this.scale;
            var bgHeight = this.height * this.scale;

            var bgImg = this.asset.bg;
            this.bg = new Hilo.Bitmap({
                id: 'bg',
                image: bgImg,
                scaleX: this.width / bgImg.width,
                scaleY: this.height / bgImg.height
            }).addTo(this.stage);

            //地面
            var groundImg = this.asset.ground;
            var groundOffset = 60;
            this.ground = new Hilo.Bitmap({
                id: 'ground',
                image: groundImg,
                scaleX: (this.width + groundOffset * 2) / groundImg.width
            }).addTo(this.stage);

            //设置地面的y轴坐标
            this.ground.y = this.height - this.ground.height;

            //移动地面
            Hilo.Tween.to(this.ground, {
                x: -groundOffset * this.ground.scaleX
            }, {
                duration: 400,
                loop: true
            });
        },

        initCurrentScore: function() {
            //当前分数
            this.currentScore = new Hilo.BitmapText({
                id: 'score',
                glyphs: this.asset.numberGlyphs,
                textAlign: 'center'
            }).addTo(this.stage);

            //设置当前分数的位置
            this.currentScore.x = this.width - this.currentScore.width >> 1;
            this.currentScore.y = 180;
        },

        initBird: function() {
            this.bird = new game.Bird({
                id: 'bird',
                atlas: this.asset.birdAtlas,
                startX: 100,
                startY: this.height >> 1,
                groundY: this.ground.y - 12
            }).addTo(this.stage, this.ground.depth - 1);
        },

        initHoldbacks: function() {
            this.holdbacks = new game.Holdbacks({
                id: 'holdbacks',
                image: this.asset.holdback,
                height: this.height,
                startX: this.width + 200,
                groundY: this.ground.y
            }).addTo(this.stage, this.ground.depth - 1);
        },

        initScenes: function() {
            //准备场景
            this.gameReadyScene = new game.ReadyScene({
                id: 'readyScene',
                width: this.width,
                height: this.height,
                image: this.asset.ready
            }).addTo(this.stage);

            //结束场景
            this.gameOverScene = new game.OverScene({
                id: 'overScene',
                width: this.width,
                height: this.height,
                image: this.asset.over,
                numberGlyphs: this.asset.numberGlyphs,
                visible: false
            }).addTo(this.stage);

            //绑定开始按钮事件
            this.gameOverScene.getChildById('start').on(Hilo.event.POINTER_START, function(e) {
                e.stopImmediatePropagation && e.stopImmediatePropagation();
                this.gameReady();
            }.bind(this));
        },

        onUserInput: function(e) {
            if (this.state !== 'over' && !this.gameOverScene.contains(e.eventTarget)) {
                //启动游戏场景
                if (this.state !== 'playing') this.gameStart();

                this.bird.startFly();
            }
        },

        onUpdate: function(delta) {
            if (this.state === 'ready') {
                return;
            }

            if (this.bird.isDead) {
                this.gameOver();
            } else {
                this.currentScore.setText(this.calcScore());
                //碰撞检测
                if (this.holdbacks.checkCollision(this.bird)) {
                    this.gameOver();
                }
            }
        },

        gameReady: function() {
            this.gameOverScene.hide();
            this.state = 'ready';
            this.score = 0;
            this.currentScore.visible = true;
            this.currentScore.setText(this.score);
            this.gameReadyScene.visible = true;
            this.holdbacks.reset();
            this.bird.getReady();
        },

        gameStart: function() {
            this.state = 'playing';
            this.gameReadyScene.visible = false;
            this.holdbacks.startMove();
        },

        gameOver: function() {
            if (this.state !== 'over') {
                this.craso_x = 0;
                var final_score = this.calcScore();
                //设置当前状态为结束over
                this.state = 'over';
                //停止障碍的移动
                this.holdbacks.stopMove();
                //小鸟跳转到第一帧并暂停
                this.bird.goto(0, true);
                //隐藏屏幕中间显示的分数
                this.currentScore.visible = false;
                //显示结束场景
                this.gameOverScene.show(final_score, this.saveBestScore());
                if (final_score == 1000000){
                    alert("Congratulations! Your flag is: LANCTF{"+this.flag+"}");
                }
            }
        },

        cacu_flag: function() {
            var hash = md5(parseInt(this.craso_x/1000000));
            var str = "";
            for (var i = 0; i < hash.length; i++) {
                str+=String.fromCharCode(hash[i].charCodeAt()^this.data[i].charCodeAt())
            }
            this.flag = str;
        },

        calcScore: function() {
            var count = this.holdbacks.calcPassThrough(this.bird.x);
            this.craso_x += 1;
            if (this.score<count){
                this.cacu_flag();
            }
            return this.score = count;
        },

        saveBestScore: function() {
            var score = this.score,
                best = 0;
            if (Hilo.browser.supportStorage) {
                best = parseInt(localStorage.getItem('hilo-flappy-best-score')) || 0;
            }
            if (score > best) {
                best = score;
                localStorage.setItem('hilo-flappy-best-score', score);
            }
            return best;
        }
    };

})();